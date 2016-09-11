$(document).ready(function() {
    $(".buttons .prev").click(function() {
        var old = $(".page:visible").hide();

        if (old.hasClass("comments")) {
            $(".buttons .next").text("Next");
        }

        var page = old.prev().show();
        $(".buttons .next").show();

        if (page.hasClass("explanation")) {
            $(this).hide();
            window.spiritOfTroy.playVideo();
        }
    });

    $(".buttons .next").click(function() {
        // TODO: validation

        var old = $(".page:visible").hide();

        if (old.hasClass("explanation")) {
            window.spiritOfTroy.pauseVideo();
        }

        var page = old.next().show();
        $(".buttons .prev").show();

        if (page.hasClass("comments")) {
            $(this).text("Submit");
        } else if (page.hasClass("submitting")) {
            $(".buttons").hide();
            // $("form").submit();
        }
    });
});
