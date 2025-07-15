import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port:3000,
    proxy: {
      // with options
      "/clear": {
        target: "http://127.0.0.1:5000/dbs_clear",
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/clear/, ""),
      },
      "/show": {
        target: "http://127.0.0.1:5000/dbs_show",
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/show/, ""),
      },
      "/api": {
        target: "http://127.0.0.1:5000/on_this_day",
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
});
