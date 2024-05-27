const path = require('path');
const { ContextExclusionPlugin } = require('webpack');

module.exports = {
    entry: '/gym_app/static/js/profile.jsx',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'static/dist'),
    },
    module: {
        rules: [
            { test: /\.css$/, use: ['style-loader', 'css-loader'] },
            {
                test: /\.(js|jsx)$/,
                exclude: /node-modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react']
                    }
                }
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx']
    },
    mode: 'development' // Change to production when deploying
};