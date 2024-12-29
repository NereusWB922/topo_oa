'use client';
import { Slider } from '@mui/material';
import React, { useCallback, useMemo, useState } from 'react';
import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

const quarters = ["2022 Q1", "2022 Q2", "2022 Q3", "2022 Q4", "2023 Q1", "2023 Q2", "2023 Q3", "2023 Q4", "2024 Q1", "2024 Q2"]

export const PDFDataset = ({ data }: { data: any }) => {
  const [range, setRange] = useState([0, quarters.length - 1]);

  const transformedData = useMemo(() => {
    if (data === null || data === undefined) return [];
    return data.map((item: any) => ({
      ...item,
      yearQuarter: `${item.year} ${item.quarter}`
    }));
  }, [data])

  const filteredData = useMemo(() => {
    if (transformedData === null || transformedData === undefined) return [];
    return transformedData.filter((item: any) => 
      quarters.indexOf(item.yearQuarter) >= range[0] &&
      quarters.indexOf(item.yearQuarter) <= range[1])
  }, [transformedData, range])

  const onRangeChange = useCallback((event: any, newValue: number | number[]) => {
    setRange(newValue as number[]);
  }, [setRange]);

  return (
    <div className='relative min-h-screen flex flex-col max-w-screen-xl mx-auto justify-center items-center w-3/4'>
      <h2 className="text-xl font-bold text-center mb-4">Quarterly Revenue and Membership Trends (2022-2024)</h2>
      <div className="flex w-1/4 mx-auto space-x-4">
        <div className="mb-2 text-lg font-semibold">Range</div>
        <Slider 
          value={range}
          onChange={onRangeChange}
          min={0}
          max={quarters.length - 1}
          step={1}
          valueLabelDisplay="auto"
          marks
          valueLabelFormat={(index) => quarters[index]}
        />
      </div>
      <ResponsiveContainer width="90%" height={450} className="bg-gray-800 p-5 rounded-lg">
        <LineChart data={filteredData}>
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
