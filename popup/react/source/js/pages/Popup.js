import reactDOM from "react-dom";

function AddPostEvent(){
    var event = document.createEvent('Event');
    event.initEvent('addPostNav', true, true);
    document.dispatchEvent(event)
}

Class AddPost extends React.Component {
    getInitialState: function(){
        return: { showModal: 'none'}
    },
    componentDidMount: function () {
        var self = this;
        document.addEventListener('addPostNav', function(e) {
            self.showModal();
        }, false);
    },
    showModal: function(){
        this.setState({ showModal: 'inherit'});
    },
    closeModal: function(){
        this.setState({ showModal: 'none' });
    }
    addPost: function(){
        var self = this;
        var date = new Date();
        date = date.toISOString();

        var sendData = {author: "", tags: $('#addPostModalTags').val(), title: $('#addNewsModalTitle').val(), article:$('#addNewsModalArticle', date: date)};

        $.ajax({
            url: 'http://www.noobpost.com/post/api/',
            dataType: 'json',
            method: 'POST',
            data: sendData,
            success: function(data){
                var id = data.id
                window.location.href = "http://www.google.com";
            }.bind(this),
            error: function(xhr, status, err){
            console.error("htljkasdf", status, err.toString());
            }.bind(this)
        });
    },
    render: function(){
        var style = { display: this.state.showModal, top: '50px' };
        var close = <button class="btn btn-default" onClick={this.closeModal}>Close</button>;
        var addPostBody = <div>
                            <label>Title:</label>
                            <input type="text" class="form-control" id="addPostModalTitle" />

                            <label>Article:</label>
                            <textarea class="form-control" style={{height: '350px'}} id="addPostModalArticle"></textarea>

                            <label>Tags:</label>
                            <input type="text" class="form-control" id="addPostModalTags" />

                            <button style={{marginTop: '20px'}} className="btn btn-primary" onclick={this.addPost}>Add Post</button>
                          </div>
        return(
            <div>
                <AddPostModal style={style} title="Add a new post" close={close} action={action} body={addPostBody} />
            </div>
        )
    }
};

var AddPostModal = React.createClass({
    render: function(){
        return(
            <div id="addMovieModal" class="modal" style="{this.props.style}">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close"></button>
                            <h4 class="modal-title">{this.props.title}</h4>
                        </div>
                        <div class="modal-body">
                            {this.props.body}
                            <br />
                            {this.props.matches}
                        </div>
                        <div class="modal-footer" style={{clear: 'both'}}>
                            {this.props.close}
                            {this.props.action}
                        </div>
                    </div>
                </div>
            </div>
        )
    }
});

ReactDOM.render(<AddPost>, document.getElementByID('addPost'));