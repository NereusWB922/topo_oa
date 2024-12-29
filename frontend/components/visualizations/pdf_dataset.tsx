import React, { useMemo } from 'react';
import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

export const PDFDataset = ({ data }: { data: any }) => {
  const transformedData = useMemo(() => {
    if (data === null || data === undefined) return [];
    return data.map((item: any) => ({
      ...item,
      yearQuarter: `${item.year} ${item.quarter}`
    }));
  }, [data])

  return (
    <div className='relative min-h-screen flex flex-col max-w-screen-xl mx-auto justify-center items-center w-3/4'>
      <h2 className="text-xl font-bold text-center mb-4">Quarterly Revenue and Membership Trends (2022-2024)</h2>
      <ResponsiveContainer width="90%" height={450} className="bg-gray-800 p-5 rounded-lg">
        <LineChart data={transformedData}>
          <CartesianGrid stroke="#444" strokeDasharray="3 3"/>
          <XAxis dataKey="yearQuarter" stroke="#ccc" tickMargin={5} />
          <Legend wrapperStyle={{ color: '#ccc', bottom: 1 }} style={{ marginTop: 10}}/>
          <YAxis yAxisId="left" dataKey="revenue_in_$" stroke="#ccc" />
          <YAxis yAxisId="right" orientation="right" dataKey="memberships_sold" stroke="#ccc" />
          <Tooltip contentStyle={{ backgroundColor: '#555', border: 'none', borderRadius: 5 }} itemStyle={{ color: '#ccc' }} />
          <Line name="Revenue (in $)" yAxisId="left" type="monotone" dataKey="revenue_in_$" stroke="#8884d8" strokeWidth={3}/>
          <Line name="Memberships Sold" yAxisId="right" type="monotone" dataKey="memberships_sold" stroke="#82ca9d" strokeWidth={3}/>
        </LineChart>
      </ResponsiveContainer>
      <p className="text-sm text-center text-gray-400 mt-4">Data Source: Dataset 3 (PDF)</p>
    </div>
  );
}
