import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  transpilePackages: ["@honest-practice/ui", "@honest-practice/api-client"],
};

export default nextConfig;
