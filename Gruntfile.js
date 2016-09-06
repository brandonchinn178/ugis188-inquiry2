module.exports = function (grunt) {
    grunt.loadNpmTasks("grunt-contrib-sass");
    grunt.loadNpmTasks("grunt-contrib-watch");

    grunt.initConfig({
        sass: {
            dist: {
                options: {
                    style: "compressed"
                },
                files: [{
                    expand: true,
                    cwd: "inquiry2/static/scss",
                    src: "**/*.scss",
                    dest: "inquiry2/static/css",
                    ext: ".css"
                }]
            }
        },
        watch: {
            sass: {
                files: "inquiry2/static/scss/**/*.scss",
                tasks: "sass"
            }
        }
    });

    grunt.registerTask("build", ["sass"]);
    grunt.registerTask("default", ["build", "watch"]);
};
