function refresh_score(){
    $.ajax({
      type: 'GET',
      url: '/API/score/'+id+'/',
      data: "num=3",
      success: function(data) {
        data.forEach(
          function(d,i){
            document.getElementById("name-"+i).innerHTML=d.name;
            document.getElementById("score-"+i).innerHTML=d.score;
          }
        );
      },
      dataType: 'json',
      contentType: 'application/json; charset=utf-8',
    });
  };

  $(document).ready(function() {
    refresh_score();
    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;

          }
        }
      }
      return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
      // test that a given url is a same-origin URL
      // url could be relative or scheme relative or absolute
      var host = document.location.host; // host + port
      var protocol = document.location.protocol;
      var sr_origin = '//' + host;
      var origin = protocol + sr_origin;
      // Allow absolute or scheme relative URLs to same origin
      return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
    }


    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
          // Send the token to same-origin, relative URLs only.
          // Send the token only if the method warrants CSRF protection
          // Using the CSRFToken value acquired earlier
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      }
    });


    window.addEventListener("message", function(event) {
      if (event.data.messageType === "SAVE") {
        $.ajax({
          type: 'POST',
          url: '/gamedata/'+id+'/',
          data: JSON.stringify(event.data.gameState),
          success: function() {
            alert("Saved! It worked.");
          },
          error:function(){
            var message =  {
              messageType: "ERROR",
              info: "Gamestate could not be saved"
            };
            document.getElementById("playframe").contentWindow.postMessage(message, "*");
          },
          dataType: 'json',
          contentType: 'application/json; charset=utf-8',


        });

      } else if (event.data.messageType === "LOAD_REQUEST") {

        $.ajax({
          type: 'GET',
          dataType: 'json',
          contentType: 'application/json; charset=utf-8',
          url: '/gamedata/'+id+'/',
          success: function(data) {
            var message = {
              messageType: "LOAD",
              gameState: data
            };
            document.getElementById("playframe").contentWindow.postMessage(message, "*");

          },
          error:function(){
            var message =  {
              messageType: "ERROR",
              info: "Gamestate could not be loaded"
            };
            document.getElementById("playframe").contentWindow.postMessage(message, "*");
          }
        });
      }
      else if (event.data.messageType === "SCORE") {
        $.ajax({
          type: 'POST',
          dataType: 'json',
          contentType: 'application/json; charset=utf-8',
          url: '/newscore/'+id+'/',
          data: JSON.stringify(event.data),
          success: function(data) {
            alert("Score Submitted!");
            document.getElementById("game-info-scores").innerHTML="<p><b>Your highest score:</b>"+data.highest.toFixed(1)+"</p>";
            refresh_score();
          }
        });

      }
      else if (event.data.messageType === "SETTING"){
		    document.getElementById("best-size").innerHTML = "<p>Best game window size is <b>"+event.data.options.width+"*"+event.data.options.height+"</b></p>";
			document.getElementById("current-size").innerHTML = "<p>Current game window size is <b>"+document.getElementById("playframe").offsetWidth+"*"+document.getElementById("playframe").offsetHeight+"</b></p>";
		  	window.addEventListener("resize", function(){
				document.getElementById("current-size").innerHTML = "<p>Current game window size is <b>"+document.getElementById("playframe").offsetWidth+"*"+document.getElementById("playframe").offsetHeight+"</b></p>";
			});
      }
    });
  });

  window.twttr = (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0],
      t = window.twttr || {};
    if (d.getElementById(id)) return t;
    js = d.createElement(s);
    js.id = id;
    js.src = "https://platform.twitter.com/widgets.js";
    fjs.parentNode.insertBefore(js, fjs);

    t._e = [];
    t.ready = function(f) {
      t._e.push(f);
    };

    return t;
  }(document, "script", "twitter-wjs"));
