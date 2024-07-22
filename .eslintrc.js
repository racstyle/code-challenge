module.exports = {
  globals: {
    __PATH_PREFIX__: true,
  },
  rules: {
    "indent": ["error", 2],
    "no-console": "off",
    "strict": ["error", "global"],
    "curly": "warn",
    "semi": ["error", "always"],  // Always use semicolons
    "space-in-parens": "off",   // Disable
    "space-before-function-paren": "off",   // Disable
    "space-before-blocks": ["error", "always"]
  },
  // To allow many operations such as async/await functions
  parserOptions: {
    ecmaVersion: 2020,
    sourceType: "module",
  },
  env: {
    browser: true,
    es6: true,
  },
}
