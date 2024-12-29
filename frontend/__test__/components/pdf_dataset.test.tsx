import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import '@testing-library/jest-dom'
import { act } from "react";
import { PDFDataset } from "@/components/visualizations/pdf_dataset";

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

const mockData = [
  { year: 2022, quarter: 'Q1', revenue_in_$: 10000, memberships_sold: 500 },
  { year: 2022, quarter: 'Q2', revenue_in_$: 12000, memberships_sold: 600 },
  { year: 2023, quarter: 'Q1', revenue_in_$: 15000, memberships_sold: 700 },
];

describe("PDFDataset Component", () => {
  it("should render the component correctly", async () => {
    await act(async () => render(<PDFDataset data={mockData} />));
    
    expect(screen.getByText("Quarterly Revenue and Membership Trends (2022-2024)")).toBeInTheDocument();
    expect(screen.getByText("Revenue (in $)")).toBeInTheDocument();
    expect(screen.getByText("Memberships Sold")).toBeInTheDocument();
  });
});
