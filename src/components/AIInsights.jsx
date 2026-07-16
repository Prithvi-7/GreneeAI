export default function AIInsights() {
  const insights = [
    {
      title: "Carbon Emissions Increased",
      description: "Carbon emissions increased by 12% compared to last month.",
      type: "warning",
    },
    {
      title: "Energy Consumption Stable",
      description: "Energy usage is within the expected monthly target.",
      type: "success",
    },
    {
      title: "ESG Score Improved",
      description: "Average ESG score increased from 82 to 85.",
      type: "info",
    },
  ];

  const badgeColor = (type) => {
    switch (type) {
      case "warning":
        return "bg-red-100 text-red-700";
      case "success":
        return "bg-green-100 text-green-700";
      default:
        return "bg-blue-100 text-blue-700";
    }
  };

  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">
      <h2 className="text-xl font-bold mb-6">
        🤖 AI Insights
      </h2>

      <div className="space-y-5">
        {insights.map((item, index) => (
          <div
            key={index}
            className="border rounded-xl p-4 hover:shadow-md transition"
          >
            <div className="flex justify-between items-center">
              <h3 className="font-bold text-gray-800">
                {item.title}
              </h3>

              <span
                className={`px-3 py-1 rounded-full text-sm ${badgeColor(
                  item.type
                )}`}
              >
                {item.type}
              </span>
            </div>

            <p className="text-gray-600 mt-2">
              {item.description}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}