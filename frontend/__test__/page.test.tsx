import Home from '@/app/page';
import '@testing-library/jest-dom'
import { render, screen, waitFor } from '@testing-library/react'
import { act } from 'react';

jest.mock('@/components/visualizations/csv_dataset', () => ({
  CSVDataset: () => <div>CSVDataset Component</div>,
}));
  
jest.mock('@/components/visualizations/json_dataset', () => ({
  JSONDataset: () => <div>JSONDataset Component</div>,
}));
  
jest.mock('@/components/visualizations/pdf_dataset', () => ({
  PDFDataset: () => <div>PDFDataset Component</div>,
}));

describe("Home Component", () => {
  beforeEach(() => {
    global.fetch = jest.fn() as jest.Mock;
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it("should show loader while fetching data", async () => {
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      json: () => new Promise((resolve) => {
        setTimeout(() => {
          resolve({ json: {}, csv: {}, pdf: {} });
        }, 3000); // Simulate a delay
      }),
    });

    await act(async () => render(<Home />));

    expect(screen.getByRole("progressbar")).toBeInTheDocument();
  });

  it("should render datasets after data is fetched", async () => {
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      json: () => Promise.resolve({ json: {}, csv: {}, pdf: {} }),
    });

    await act(async () => render(<Home />));

    await waitFor(() => expect(screen.queryByRole("progressbar")).not.toBeInTheDocument());

    expect(screen.getByText("JSONDataset Component")).toBeInTheDocument();
    expect(screen.getByText("CSVDataset Component")).toBeInTheDocument();
    expect(screen.getByText("PDFDataset Component")).toBeInTheDocument();
  });
});