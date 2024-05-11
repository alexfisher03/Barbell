const path = require('path');

module.exports = {
    entry: '/gym_app/static/js/profile.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'static/dist'),
    },
    module: {
        rules: [
            { test: /\.css$/, use: ['style-loader', 'css-loader'] }
        ]
    },
    mode: 'production' // Change to production when deploying
};