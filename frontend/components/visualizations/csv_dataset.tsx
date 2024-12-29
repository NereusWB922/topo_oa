import React, { useMemo } from 'react'
import { Bar, BarChart, CartesianGrid, Legend, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

export const CSVDataset = ({ data } : { data: any}) => {
  const transformedData = useMemo(() => {
    if (data === null || data === undefined) return [];

    const groupByMembershipType = data.reduce((acc: any, item: any) => {
      if (!acc[item.membership_type]) {
        acc[item.membership_type] = { total_revenue: 0, total_duration: 0 };
      }
      acc[item.membership_type].total_revenue += item.revenue;
      acc[item.membership_type].total_duration += item.duration_minutes;
      return acc;
    }, {});

    const transformedData = [];

    for (const [key, value] of Object.entries(groupByMembershipType)) {
      transformedData.push({ membership_type: key, total_revenue: (value as any).total_revenue.toFixed(2), total_duration: (value as any).total_duration });
    }

    return transformedData; 
  }, [data]);

  return (
    <div className='relative min-h-screen flex flex-col max-w-screen-xl mx-auto justify-center items-center w-3/4'>
      <h2 className="text-xl font-bold text-center mb-4">Total Revenue and Duration by Membership Type (Jan 2024)</h2>
      <ResponsiveContainer width="70%" height={450} className="bg-gray-800 p-5 rounded-lg">
        <BarChart data={transformedData}>
          <CartesianGrid stroke="#444" strokeDasharray="3 3"/>
          <XAxis dataKey="membership_type" stroke="#ccc" tickMargin={5} />
          <YAxis yAxisId="left" dataKey="total_revenue" stroke="#ccc" />
          <Tooltip contentStyle={{ backgroundColor: '#555', border: 'none', borderRadius: 5  }} itemStyle={{ color: '#ccc' }} />
          <Bar name="Total Revenue (in $)" yAxisId="left" dataKey="total_revenue" fill="#8884d8"/>
          <Bar name="Total Duration (in Minutes)" yAxisId="left" dataKey="total_duration" fill="#82ca9d"/>
          <Legend wrapperStyle={{ color: '#ccc', bottom: 1 }} style={{ marginTop: 10}}/>
        </BarChart>
      </ResponsiveContainer>
      <p className="text-sm text-center text-gray-400 mt-4">Data Source: Dataset 2 (CSV)</p>
    </div>
  );
}
