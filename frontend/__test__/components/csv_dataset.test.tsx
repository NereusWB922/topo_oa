import React, { act } from "react";
import '@testing-library/jest-dom'
import { render, screen } from "@testing-library/react";
import { CSVDataset } from "@/components/visualizations/csv_dataset";

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

describe("CSVDataset", () => {
  const mockData = [
    { membership_type: "Basic", revenue: 200, duration_minutes: 150 },
    { membership_type: "VIP", revenue: 150, duration_minutes: 100 },
    { membership_type: "Premium", revenue: 120, duration_minutes: 90 },
  ];

  it("should render the chart and process the data correctly", async() => {
    await act(async () => render(<CSVDataset data={mockData} />));

    expect(screen.getByText("Total Revenue and Duration by Membership Type (Jan 2024)")).toBeInTheDocument();
    expect(screen.getByText("Basic")).toBeInTheDocument();
    expect(screen.getByText("VIP")).toBeInTheDocument();
    expect(screen.getByText("Premium")).toBeInTheDocument();
    expect(screen.getByText("Total Revenue (in $)")).toBeInTheDocument();
    expect(screen.getByText("Total Duration (in Minutes)")).toBeInTheDocument();
    expect(screen.getByText("Data Source: Dataset 2 (CSV)")).toBeInTheDocument();
  });

  it("should render an empty chart without crashing if no data is passed", async () => {
    await act(async () => render(<CSVDataset data={null} />));

    expect(screen.getByText("Total Revenue and Duration by Membership Type (Jan 2024)")).toBeInTheDocument();
    expect(screen.getByText("Total Revenue (in $)")).toBeInTheDocument();
    expect(screen.getByText("Total Duration (in Minutes)")).toBeInTheDocument();
    expect(screen.getByText("Data Source: Dataset 2 (CSV)")).toBeInTheDocument();
    expect(screen.queryByText("Basic")).toBeNull();
    expect(screen.queryByText("VIP")).toBeNull();
    expect(screen.queryByText("Premium")).toBeNull();
  });
});
