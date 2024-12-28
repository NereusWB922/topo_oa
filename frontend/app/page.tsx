'use client';
import PDF_Dataset from "@/components/pdf_dataset";
import { useEffect, useState } from "react";

export default function Home() {
  const [data, setData] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/data`)
      .then((res) => res.json())
      .then((data) => {
        console.log(data)
        setData(data)
        setIsLoading(false)
      })
  }, [])

  return (
    <div className="snap-y snap-mandatory overflow-y-scroll h-screen">
        <div className="snap-always snap-center">
          <PDF_Dataset data={data?.pdf} />
        </div>
    </div>
  );
}
