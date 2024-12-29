'use client';
import { CSVDataset } from "@/components/visualizations/csv_dataset";
import { JSONDataset } from "@/components/visualizations/json_dataset";
import { PDFDataset } from "@/components/visualizations/pdf_dataset";
import { useEffect, useState } from "react";

export default function Home() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/data`)
      .then((res) => res.json())
      .then((data) => {
        setData(data)
      })
  }, [])

  return (
    <div className="snap-y snap-mandatory overflow-y-scroll h-screen">
      <div className="snap-always snap-center">
          <JSONDataset data={data?.json} />
        </div>
        <div className="snap-always snap-center">
          <CSVDataset data={data?.csv} />
        </div>
        <div className="snap-always snap-center">
          <PDFDataset data={data?.pdf} />
        </div>
    </div>
  );
}
