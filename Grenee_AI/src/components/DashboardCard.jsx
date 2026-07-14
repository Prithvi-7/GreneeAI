const gradients = {
  "Organizations": "from-green-500 to-emerald-600",
  "Employees": "from-blue-500 to-cyan-600",
  "Carbon Footprint": "from-red-500 to-rose-600",
  "Energy Usage": "from-yellow-400 to-orange-500",
  "Average ESG Score": "from-purple-500 to-indigo-600",
  "Compliance Status": "from-teal-500 to-green-600",
};

export default function DashboardCard({
  title,
  value,
  icon,
}) {

  const gradient =
    gradients[title] || "from-gray-500 to-gray-700";

  return (
    <div
      className={`
        bg-gradient-to-r
        ${gradient}
        rounded-2xl
        shadow-xl
        p-6
        text-white
        hover:scale-105
        hover:shadow-2xl
        transition-all
        duration-300
      `}
    >
      <div className="flex justify-between items-center">

        <div>

          <h3 className="text-white/80 text-sm uppercase font-semibold">
            {title}
          </h3>

          <h1 className="text-4xl font-bold mt-3">
            {value}
          </h1>

          <p className="mt-5 text-sm text-white/90">
            ▲ 12% compared to last month
          </p>

        </div>

        <div className="bg-white/20 rounded-full w-20 h-20 flex items-center justify-center text-5xl">
          {icon}
        </div>

      </div>
    </div>
  );
}