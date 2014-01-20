Template.postSubmit.events({
    'submit form': function(e) {
        e.preventDefault();

        var post = {
            url: $(e.target).find('[name=url]').val(),
            url: $(e.target).find('[name=title]').val(),
            url: $(e.target).find('[name=message]').val()
        }

        post._id = Posts.insert(post);
        Router.go('postPage', post);
    }
});