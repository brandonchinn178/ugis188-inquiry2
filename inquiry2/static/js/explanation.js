var onYouTubeIframeAPIReady = function() {
    var player = window.spiritOfTroy = new YT.Player("spirit-of-troy", {
        height: "350",
        width: "500",
        videoId: "KUFqIYBCw_o",
        events: {
            onReady: function() {
                player.mute();
                player.playVideo();
                player.setLoop(true);
            },
            onStateChange: function(e) {
                if (e.data === YT.PlayerState.ENDED) {
                    // loop video
                    player.playVideo();
                }
            },
        },
    });
};
