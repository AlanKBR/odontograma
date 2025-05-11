module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  extends: ["eslint:recommended"],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: "script",
  },
  rules: {
    "indent": ["error", 2],
    "linebreak-style": ["error", "windows"],
    "quotes": ["error", "single"],
    "semi": ["error", "always"],
    "no-console": "off",
    "no-undef": "off" // Since we're dealing with older browser scripts
  }
};
