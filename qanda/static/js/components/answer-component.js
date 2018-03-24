

Vue.component('AnswerComponent',{

    template: `
    <div class="row">
        <div class="col-xs-12 col-sm-8 col-md-8">
            <div class="box box-default  no-border">
                <div class="box-header with-border">
                    <h3 class="box-title expandable">
                    <img v-if="this.image !== '' " src="../../dist/img/user2-160x160.jpg" class="img-circle" 
                        alt="User Image">, {{ this.userTitle }}, {{ this.pubDate }} .
                    </h3>
                <div class="box-tools pull-right">
                    <button type="button" class="btn btn-box-tool" data-widget="collapse"><i class="fa fa-plus"></i>
                    </button>
                </div>
            </div>
            <div class="box-body">
                <div>
                    {{ this.details }}
                </div>
                <i class=""></i>
                <p>
                    <a class="btn aboutcm-active btn-sm text-white">
                        <i class="ion-thumbsup"></i> {{ this.nbUpvotes }}
                    </a>&nbsp;
                    <a class="btn btn-danger btn-sm  text-white">
                        <i class="ion-thumbsdown"></i> {{ this.nbDownvotes }}</a>
                    <span class='float-right'>                        
                    <a class="btn btn-sm btn-social-icon btn-facebook"><i class="fa fa-facebook"></i></a>                        <a class="btn btn-white text-primary"><i class='ion-social-twitter'></i></a>
                    <a class="btn btn-white text-danger"><i class="ion-social-googleplus"></i></a>
                </span>
                </p>
                <div class="highlight">
                    <form>
                        <input type="text" class="form-control">
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</div>
    `,
data: function(){
    return {
        id: "",
        details:"",
        nbUpvotes: 0,
        nbDownvotes: 0,
        pubDate: "",
        userPicture: "",
        userTitle:""
    }
}
})