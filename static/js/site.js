$(document).ready(function(){
    $('#send-message').click(function(){
        var userMessage = showUserMessage();
    });
});

var countMessages = 0;
function showUserMessage(){
    var messageText = "Вы: " + $('#user-message').val();
    var messageId = "messageId-" + countMessages;
    var messageBlock = $('<div>', {'class':'message', 'id':messageId}).prependTo('.chat-window');
    var userMessageBlock = $('<div>', {'class':'user-message'}).prependTo(messageBlock);
    $('<p>', {'text':messageText}).prependTo(userMessageBlock);
    $('#user-message').val("");
    countMessages++;
    return messageText;
}

function sendUserMessageAjax(userMessage){

}
