export default function AdminProfile() {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">

      <div className="flex flex-col items-center">

        <div className="w-24 h-24 rounded-full bg-gradient-to-r from-green-600 to-emerald-500 flex items-center justify-center text-5xl text-white shadow-lg">
          👤
        </div>

        <h2 className="mt-5 text-2xl font-bold text-gray-800">
          Admin
        </h2>

        <p className="text-gray-500">
          ESG Administrator
        </p>

      </div>

      <div className="mt-8 space-y-4">

        <div className="flex justify-between border-b pb-2">
          <span className="font-semibold text-gray-600">
            Name
          </span>

          <span className="text-gray-800">
            Anusiya
          </span>
        </div>

        <div className="flex justify-between border-b pb-2">
          <span className="font-semibold text-gray-600">
            Email
          </span>

          <span className="text-gray-800">
            admin@grenee.ai
          </span>
        </div>

        <div className="flex justify-between border-b pb-2">
          <span className="font-semibold text-gray-600">
            Role
          </span>

          <span className="text-green-600 font-semibold">
            Administrator
          </span>
        </div>

        <div className="flex justify-between">
          <span className="font-semibold text-gray-600">
            Last Login
          </span>

          <span className="text-gray-800">
            Today 09:15 AM
          </span>
        </div>

      </div>

    </div>
  );
}