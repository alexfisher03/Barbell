const path = require('path');

module.exports = {
    entry: {
        profile: './gym_app/static/js/profile.jsx',
        inputWorkouts: '/gym_app/static/js/input-workouts.jsx'
    },
    output: {
        filename: '[name].bundle.js',
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

  mode: 'production' // Change to production when deploying


};