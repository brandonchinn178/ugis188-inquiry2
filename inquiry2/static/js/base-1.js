var REQUIRED_MESSAGE = "Y U NO ANSWER QUESTION??";

$(document).ready(function() {
    $(".buttons .prev").click(function() {
        var page = $(".page:visible").hide();

        if (page.hasClass("comments")) {
            $(".buttons .next").text("Next");
        }

        var nextPage = page.prev().show();
        $(".buttons .next").show();

        if (nextPage.hasClass("explanation")) {
            $(this).hide();
            window.spiritOfTroy.playVideo();
        }
    });

    $(".buttons .next").click(function() {
        $(".messages").empty();
        var page = $(".page:visible");

        if (!isValid(page)) {
            $("<li>")
                .text(REQUIRED_MESSAGE)
                .appendTo(".messages");
            return;
        }

        page.hide();

        if (page.hasClass("explanation")) {
            window.spiritOfTroy.pauseVideo();
        }

        var nextPage = page.next().show();
        $(".buttons .prev").show();

        if (nextPage.hasClass("comments")) {
            $(this).text("Submit");
        } else if (nextPage.hasClass("submitting")) {
            $(".buttons").hide();
            // $("form").submit();
        }
    });
});

/**
 * Validates each page as the next button is pressed
 */
var isValid = function(page) {
    if (page.hasClass("meme") || page.hasClass("details")) {
        return page.find("input:checked").length === 2;
    } else if (page.hasClass("name")) {
        return page.find("input").val() !== "";
    }
    return true;
};
