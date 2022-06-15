module.exports = {
  root: true,
  extends: [
    "plugin:vue/base",
    "plugin:vue/vue3-essential",
    "plugin:vue/vue3-strongly-recommended",
    "plugin:vue/vue3-recommended",
    "plugin:prettier/recommended",
    "eslint:recommended",
  ],
  env: {
    node: true,
    browser: true,
    commonjs: true,
    amd: true,
  },
};
