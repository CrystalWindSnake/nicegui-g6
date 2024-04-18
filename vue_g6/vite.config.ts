import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    cssCodeSplit: false,

    lib: {
      // Could also be a dictionary or array of multiple entry points
      entry: "src/libs/main.ts",
      formats: ["es"],
      // name: 'UseDraggable',
      // the proper extensions will be added
      fileName: "g6",
      // fileName(format, entryName) {
      //   return  entryName
      // },
    },
    rollupOptions: {
      // 确保外部化处理那些你不想打包进库的依赖
      external: ["vue"],
      output: {
        // 在 UMD 构建模式下为这些外部化的依赖提供一个全局变量
        globals: {
          vue: "Vue",
        },
      },
    },
  },
});
