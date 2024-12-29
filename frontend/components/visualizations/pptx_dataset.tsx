import React, { useMemo } from 'react'
import { Legend, Pie, PieChart, ResponsiveContainer, Tooltip } from 'recharts'

export const PPTXDataset = ({ data } : { data: any}) => {
  const transformedData = useMemo(() => {
    if (data === null || data === undefined) return [];
    const transformedData = [];
    for (const [key, value] of Object.entries(data.revenue_distribution)) {
      transformedData.push({ activity: key, percentage: value });
    }
    return transformedData;
  }, [data]);

  return (
    <div className='relative min-h-screen flex flex-col max-w-screen-xl mx-auto justify-center items-center w-3/4'>
      <h2 className="text-xl font-bold text-center mb-4">Revenue Distribution by Activity (2023)</h2>
      <ResponsiveContainer width="70%" height={450} className="bg-gray-800 p-5 rounded-lg">
          <PieChart>
            <Pie data={transformedData} dataKey="percentage" nameKey="activity" fill="#8884d8" label/>
          </PieChart>
      </ResponsiveContainer>
      <p className="text-sm text-center text-gray-400 mt-4">Data Source: Dataset 4 (PPTX)</p>
    </div>
  )
}
