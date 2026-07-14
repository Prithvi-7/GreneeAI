export default function QuickActions() {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">
      <h2 className="text-xl font-bold mb-5">
        ⚡ Quick Actions
      </h2>

      <div className="grid gap-4">

        <button className="bg-green-600 hover:bg-green-700 text-white p-3 rounded-xl transition duration-300">
          + Add Organization
        </button>

        <button className="bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-xl transition duration-300">
          + Add Employee
        </button>

        <button className="bg-orange-500 hover:bg-orange-600 text-white p-3 rounded-xl transition duration-300">
          Generate ESG Report
        </button>

        <button className="bg-purple-600 hover:bg-purple-700 text-white p-3 rounded-xl transition duration-300">
          AI Sustainability Copilot
        </button>

      </div>
    </div>
  );
}