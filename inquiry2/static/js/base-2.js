var REQUIRED_MESSAGE = "It'd be gr9 if you could answer every question";

$(document).ready(function() {
    // fade out explanation as scroll
    $(window).scroll(function() {
        var ratio = $(this).scrollTop() / 475;
        var explanation = $(".explanation").css("opacity", 1 - ratio);
        $(".survey").css("opacity", ratio);

        if (
            window.spiritOfTroy === undefined ||
            window.spiritOfTroy.pauseVideo === undefined ||
            window.spiritOfTroy.playVideo === undefined
        ) {
            return;
        }
        var opacity = explanation.css("opacity");
        if (opacity <= 0) {
            window.spiritOfTroy.pauseVideo();
        } else if (opacity > 0) {
            window.spiritOfTroy.playVideo();
        }
    });

    $("table.scale button").click(function() {
        var table = $(this).parents("table");
        var name = $(this).attr("name");

        // move active button class
        table.find("button[name=" + name + "]").removeClass("active");
        $(this).addClass("active");

        // set input value
        $("input[name=" + name + "]").val($(this).text());
    });

    // don't submit when clicking enter
    $(".details input").keydown(function(e) {
        if (e.keyCode === 13) {
            e.preventDefault();
        }
    });

    $(".buttons .submit").click(function() {
        $(".messages").empty();
        if (!isValid()) {
            $("<li>")
                .text(REQUIRED_MESSAGE)
                .appendTo(".messages");
            return false;
        }

        // show submitting page
        $(".explanation, .survey").hide();
        $(".submitting").show();
    });
});

var isValid = function() {
    var empty = $("input:hidden").filter(function() {
        return $(this).val() === "";
    });

    if (empty.length > 0) {
        return false;
    }

    return $(".details input[name=name]").val() !== "";
};
