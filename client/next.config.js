/** @type {import('next').NextConfig} */
const nextConfig = {
  webpack: (config, { dev }) => {
    if (dev) {
      // Increase the polling interval to detect changes more frequently
      config.watchOptions = {
        poll: 1000, // Check for changes every second
        aggregateTimeout: 300, // Delay rebuild by 300ms
      };

      // Only output minimal logging in development mode
      config.stats = 'minimal';
    }

    return config;
  },
}

module.exports = nextConfig
