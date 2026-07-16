const notifications = [
  {
    title: "New Employee Added",
    time: "10 mins ago",
    color: "bg-green-500",
  },
  {
    title: "ESG Report Generated",
    time: "30 mins ago",
    color: "bg-blue-500",
  },
  {
    title: "Carbon Updated",
    time: "1 hour ago",
    color: "bg-red-500",
  },
  {
    title: "Energy Bill Uploaded",
    time: "Today",
    color: "bg-yellow-500",
  },
];

export default function Notifications() {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">
      <h2 className="text-xl font-bold mb-6">
        🔔 Notifications
      </h2>

      <div className="space-y-4">
        {notifications.map((item, index) => (
          <div
            key={index}
            className="flex items-center gap-4 border-b pb-3"
          >
            <div
              className={`w-3 h-3 rounded-full ${item.color}`}
            ></div>

            <div className="flex-1">
              <p className="font-semibold text-gray-700">
                {item.title}
              </p>

              <span className="text-sm text-gray-500">
                {item.time}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}