import Header from "../components/Header";
import Sidebar from "../components/Sidebar";

import CarbonChart from "../components/CarbonChart";
import ESGScoreCard from "../components/ESGScoreCard";
import EmissionDonut from "../components/EmissionDonut";
import SupplierTable from "../components/SupplierTable";

export default function ExecutiveDashboard() {
  return (
    <div className="min-h-screen bg-[#f5f7fb]">

      <Header />

      <div className="flex">

        <Sidebar />

        <main className="flex-1 p-8">

          {/* Title */}
          <div className="flex justify-between items-center mb-8">

            <div>

              <h1 className="text-4xl font-bold text-gray-800">
                ESG Overview Dashboard
              </h1>

              <p className="text-gray-500 mt-2">
                Real-time carbon accounting and sustainability metrics.
              </p>

            </div>

            <button className="bg-green-500 hover:bg-green-600 text-white px-6 py-3 rounded-xl font-semibold shadow-lg">
              Export CSRD Report
            </button>

          </div>

          {/* Top */}
          <div className="grid grid-cols-3 gap-6">

            <div className="col-span-2">
              <CarbonChart />
            </div>

            <ESGScoreCard />

          </div>

          {/* Bottom */}
          <div className="grid grid-cols-3 gap-6 mt-6">

            <div className="col-span-2">
              <SupplierTable />
            </div>

            <EmissionDonut />

          </div>

        </main>

      </div>

    </div>
  );
}