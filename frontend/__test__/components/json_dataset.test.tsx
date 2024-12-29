import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import '@testing-library/jest-dom'
import { JSONDataset } from "@/components/visualizations/json_dataset";
import { act } from "react";

// ResponsiveContainer needs fixed width and height when rendering from the tests
jest.mock('recharts', () => {
  const OriginalModule = jest.requireActual('recharts')
  return {
      ...OriginalModule,
      ResponsiveContainer: ({ children } : { children: React.ReactNode }) => (
          <OriginalModule.ResponsiveContainer width={800} height={800}>
              {children}
          </OriginalModule.ResponsiveContainer>
      ),
  }
})

beforeAll(() => {
  global.ResizeObserver = jest.fn().mockImplementation(() => ({
    observe: jest.fn(),
    unobserve: jest.fn(),
    disconnect: jest.fn(),
  }));
});
  
afterAll(() => {
  jest.restoreAllMocks();
});

const mockData = {
  companies: [
    {
      name: "Company A",
      employees: [
        {
          name: "Alice",
          role: "Engineer",
          salary: 70000,
          hired_date: "2017-05-15",
        },
        {
          name: "Bob",
          role: "Designer",
          salary: 65000,
          hired_date: "2020-03-10",
        },
      ],
    },
    {
      name: "Company B",
      employees: [
        {
          name: "Charlie",
          role: "Engineer",
          salary: 75000,
          hired_date: "2018-07-22",
        },
        {
          name: "Dave",
          role: "Manager",
          salary: 80000,
          hired_date: "2022-01-17",
        },
      ],
    },
  ],
};

describe("JSONDataset Component", () => {
  it("should render the component correctly", async () => {
    await act(async () => render(<JSONDataset data={mockData} />));
    
    expect(screen.getByText("Employee Salary vs. Hiring Date by Company")).toBeInTheDocument();
    expect(screen.getByText("Company A")).toBeInTheDocument();
    expect(screen.getByText("Company B")).toBeInTheDocument();
  });

  it("should show tooltip on hover", async () => {
    await act(async () => render(<JSONDataset data={mockData} />));

    const scatterPoints = screen.getAllByRole("img");

    fireEvent.mouseOver(scatterPoints[0]);

    await waitFor(() => {
      expect(screen.getByText("Alice")).toBeInTheDocument();
      expect(screen.getByText("Engineer")).toBeInTheDocument();
      expect(screen.getByText("$70000")).toBeInTheDocument();
    });
  });
});
