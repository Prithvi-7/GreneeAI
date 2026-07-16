export default function MonthlyAnalytics() {
  const analytics = [
    {
      department: "HR",
      esg: 88,
      carbon: 120,
      energy: 95,
      status: "Excellent",
    },
    {
      department: "Finance",
      esg: 81,
      carbon: 95,
      energy: 70,
      status: "Good",
    },
    {
      department: "IT",
      esg: 93,
      carbon: 210,
      energy: 180,
      status: "Excellent",
    },
    {
      department: "Operations",
      esg: 76,
      carbon: 165,
      energy: 140,
      status: "Average",
    },
  ];

  const statusColor = (status) => {
    switch (status) {
      case "Excellent":
        return "bg-green-100 text-green-700";
      case "Good":
        return "bg-blue-100 text-blue-700";
      default:
        return "bg-yellow-100 text-yellow-700";
    }
  };

  return (
    <div className="bg-white rounded-2xl shadow-lg p-6 mt-10">
      <h2 className="text-2xl font-bold mb-6">
        📈 Monthly Analytics
      </h2>

      <div className="overflow-x-auto">
        <table className="w-full border-collapse">

          <thead>
            <tr className="bg-green-600 text-white">
              <th className="p-3 text-left">Department</th>
              <th className="p-3">ESG</th>
              <th className="p-3">Carbon</th>
              <th className="p-3">Energy</th>
              <th className="p-3">Status</th>
            </tr>
          </thead>

          <tbody>
            {analytics.map((row, index) => (
              <tr
                key={index}
                className="border-b hover:bg-gray-50 transition"
              >
                <td className="p-4 font-semibold">
                  {row.department}
                </td>

                <td className="text-center">
                  {row.esg}
                </td>

                <td className="text-center">
                  {row.carbon}
                </td>

                <td className="text-center">
                  {row.energy}
                </td>

                <td className="text-center">
                  <span
                    className={`px-3 py-1 rounded-full text-sm font-semibold ${statusColor(
                      row.status
                    )}`}
                  >
                    {row.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>

        </table>
      </div>
    </div>
  );
}