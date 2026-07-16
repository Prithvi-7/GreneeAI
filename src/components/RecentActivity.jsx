export default function RecentActivity() {
  const activities = [
    "Organization added successfully",
    "New employee registered",
    "ESG report generated",
    "Energy bill uploaded",
    "Carbon emission updated",
  ];

  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">
      <h2 className="text-xl font-bold mb-5">
        📋 Recent Activities
      </h2>

      <div className="space-y-4">
        {activities.map((activity, index) => (
          <div
            key={index}
            className="border-l-4 border-green-600 bg-gray-50 p-3 rounded-lg"
          >
            {activity}
          </div>
        ))}
      </div>
    </div>
  );
}