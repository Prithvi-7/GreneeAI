import {
  FiGrid,
  FiUsers,
  FiHome,
  FiBarChart2,
  FiActivity,
  FiZap,
  FiFileText,
  FiCpu,
  FiSettings,
  FiLogOut,
} from "react-icons/fi";

export default function Sidebar() {
  const menu = [
    { icon: <FiGrid />, title: "Dashboard", active: true },
    { icon: <FiUsers />, title: "Employees" },
    { icon: <FiHome />, title: "Organizations" },
    { icon: <FiBarChart2 />, title: "ESG" },
    { icon: <FiActivity />, title: "Carbon" },
    { icon: <FiZap />, title: "Energy" },
    { icon: <FiFileText />, title: "Reports" },
    { icon: <FiCpu />, title: "AI Copilot" },
  ];

  return (
    <aside className="w-72 bg-white shadow-xl border-r border-gray-100 min-h-screen flex flex-col justify-between">

      <div>

        {/* Logo */}

        <div className="px-8 py-8 border-b border-gray-100">

          <h1 className="text-3xl font-extrabold text-green-600">
            🌱 Grenee AI
          </h1>

          <p className="text-gray-500 mt-2 text-sm">
            ESG Intelligence Platform
          </p>

        </div>

        {/* Menu */}

        <div className="px-5 py-6 space-y-2">

          {menu.map((item, index) => (

            <button
              key={index}
              className={`w-full flex items-center gap-4 px-5 py-4 rounded-2xl transition-all duration-300 text-lg

              ${
                item.active
                  ? "bg-green-600 text-white shadow-lg"
                  : "text-gray-600 hover:bg-green-50 hover:text-green-600"
              }
              
              `}
            >

              <span className="text-2xl">
                {item.icon}
              </span>

              <span className="font-semibold">
                {item.title}
              </span>

            </button>

          ))}

        </div>

      </div>

      {/* Bottom */}

      <div className="px-5 pb-8 space-y-2">

        <button className="w-full flex items-center gap-4 px-5 py-4 rounded-2xl text-gray-600 hover:bg-gray-100 transition">

          <FiSettings className="text-2xl" />

          <span className="font-semibold">
            Settings
          </span>

        </button>

        <button className="w-full flex items-center gap-4 px-5 py-4 rounded-2xl text-red-500 hover:bg-red-50 transition">

          <FiLogOut className="text-2xl" />

          <span className="font-semibold">
            Logout
          </span>

        </button>

      </div>

    </aside>
  );
}