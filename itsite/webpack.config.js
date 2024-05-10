const path = require('path');
const StatsPlugin = require('webpack-stats-plugin').StatsWriterPlugin;

module.exports = {
  mode: 'development',
   entry: {
    footer: './itsite/main/static/js/footer.jsx', // Точка входа для App.jsx
    header: './itsite/main/static/js/header.jsx' // Точка входа для Header.jsx
  },
  output: {
    path: path.resolve(__dirname, 'main/static/bundles'),
    filename: '[name].bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react']
          }
        },
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: 'asset/resource',
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
  plugins: [
    new StatsPlugin({
      filename: 'webpack-stats.json',
    }),
  ],
};
