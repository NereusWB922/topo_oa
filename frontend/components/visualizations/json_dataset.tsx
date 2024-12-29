import React, { useMemo } from 'react'
import { CartesianGrid, Legend, ResponsiveContainer, Scatter, ScatterChart, Tooltip, TooltipProps, XAxis, YAxis } from 'recharts';

const CustomTooltip = ({ payload, active } : TooltipProps<any, any>) => {
  if (active && payload && payload.length) {
    const { name, role, salary, hired_date } = payload[0].payload;

    return (
      <div className="custom-tooltip bg-[#555] border-none p-3 rounded-md">
        <h4 className="m-0 text-white">{name}</h4>
        <p className="m-0 text-gray-300"><strong>Role:</strong> {role}</p>
        <p className="m-0 text-gray-300"><strong>Salary:</strong> ${salary}</p>
        <p className="m-0 text-gray-300"><strong>Hired on:</strong> {new Date(hired_date).toLocaleDateString()}</p>
      </div>
    );
  }

  return null;
};

export const JSONDataset = ({ data }: { data: any }) => {
  const transformedData = useMemo(() => {
    if (data === null || data === undefined) return [];
    return data.companies.map((company: any) => {
      return {
        ...company,
        employees: company.employees.filter((employee: any) => employee.hired_date).map((employee: any) => ({
          ...employee,
          hired_date: new Date(employee.hired_date).getTime()
        }))
      }
    });

  }, [data]);

  return (
    <div className='relative min-h-screen flex flex-col max-w-screen-xl mx-auto justify-center items-center w-3/4'>
      <h2 className="text-xl font-bold text-center mb-4">Employee Salary vs. Hiring Date by Company</h2>
      <ResponsiveContainer width="90%" height={450} className="bg-gray-800 p-5 rounded-lg">
        <ScatterChart>
          <CartesianGrid stroke="#444" strokeDasharray="3 3"/>
          <XAxis dataKey="hired_date" type="number" name="Hired Date" stroke="#ccc" domain={['auto', 'auto']} tickFormatter={(tick) => new Date(tick).toLocaleDateString()} />
          <YAxis dataKey="salary" type="number" name="Salary" stroke="#ccc" />
          <Scatter data={transformedData[0]?.employees} name={transformedData[0]?.name} fill="#8884d8"/>
          <Scatter data={transformedData[1]?.employees} name={transformedData[1]?.name}  fill="#82ca9d"/>
          <Legend wrapperStyle={{ color: '#ccc', bottom: 1 }} style={{ marginTop: 10}}/>
          <Tooltip content={<CustomTooltip />}/>
        </ScatterChart>
      </ResponsiveContainer>
      <p className="text-sm text-center text-gray-400 mt-4">Data Source: Dataset 1 (JSON)</p>
    </div>
  );
}

