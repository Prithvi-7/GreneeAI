import {
  FiBell,
  FiSearch,
  FiSettings,
  FiChevronDown,
} from "react-icons/fi";

import "@fontsource/inter";

export default function Header() {
  return (
    <header className="sticky top-0 z-50 bg-white border-b border-gray-200 shadow-sm">

      <div className="flex items-center justify-between px-8 h-20">

        {/* Left */}

        <div className="flex items-center gap-10">

          <div>
            <h1 className="text-3xl font-extrabold text-green-600 tracking-tight">
              🌱 Grenee AI
            </h1>

            <p className="text-sm text-gray-500">
              ESG Intelligence Platform
            </p>
          </div>

          <div className="hidden lg:flex items-center bg-gray-100 rounded-2xl px-5 py-3 w-[420px]">

            <FiSearch className="text-gray-500 text-xl" />

            <input
              type="text"
              placeholder="Search employees, reports..."
              className="bg-transparent outline-none ml-3 w-full text-gray-700"
            />

          </div>

        </div>

        {/* Right */}

        <div className="flex items-center gap-5">

          <button className="w-12 h-12 rounded-xl bg-gray-100 hover:bg-green-100 transition flex items-center justify-center">
            <FiBell className="text-xl text-gray-700" />
          </button>

          <button className="w-12 h-12 rounded-xl bg-gray-100 hover:bg-green-100 transition flex items-center justify-center">
            <FiSettings className="text-xl text-gray-700" />
          </button>

          <div className="flex items-center gap-3 bg-gray-100 rounded-2xl px-4 py-2 cursor-pointer hover:bg-green-50 transition">

            <div className="w-12 h-12 rounded-full bg-green-600 flex items-center justify-center text-white font-bold text-lg">
              A
            </div>

            <div className="hidden md:block">
              <h3 className="font-bold text-gray-800">
                Anusiya
              </h3>

              <p className="text-sm text-gray-500">
                ESG Administrator
              </p>
            </div>

            <FiChevronDown className="text-gray-600" />

          </div>

        </div>

      </div>

    </header>
  );
}