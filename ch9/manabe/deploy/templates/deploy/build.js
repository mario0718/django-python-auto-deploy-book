$(".buildBtn").click(function(e){
    $("#modal_app_name").html($(this).attr('app_name'));
    $("#modal_deploy_version").html($(this).attr('deploy_version'));
    var jenkins_job_console = '{{jenkins_url}}' + $(this).attr('jenkins_job') + '/lastBuild/console '
    $("#modal_jenkins_job").html($(this).attr('jenkins_job'));
    $("#modal_jenkins_url").html(jenkins_job_console);
     $("#modal-demo").modal("show");
});

function modal_close(){
	$("#modal-demo").modal("hide");
	location.reload();
}

$(".checkBtn").click(function(e){
    var app_name = $(this).attr('app_name');
    var deploy_version = $(this).attr('deploy_version');
    var check_url = '{{nginx_url}}/' + app_name + '/' + deploy_version + '/';
    openFullScreen(check_url)

});

function openFullScreen (url) {
    var name = arguments[1] ? arguments[1] : "_blank";
    var feature = "fullscreen=no,channelmode=no, titlebar=no, toolbar=no, scrollbars=no," +
         "resizable=yes, status=no, copyhistory=no, location=no, menubar=no,width=1000 " +
         "height=400, top=0, left=200";
    var newWin = window.open(url, name, feature);
}
$(".btn_gen_pkg").click(function(){
    var deploy_version = $("#modal_deploy_version").text();
    var app_name = $("#modal_app_name").text();
    var jenkins_job = $("#modal_jenkins_job").text();

    promiseJenkins = $.ajax({
        url:'{% url 'deploy:jenkins_build' %}',
        type: 'post',
        data:{
            deploy_version: deploy_version,
            jenkins_job: jenkins_job,
            app_name:app_name
        },
        dataType: 'json',
        beforeSend: function(){
            $(".btn_gen_pkg").attr("disabled","disabled");
             $(".btn_gen_pkg").hide();
            $("#build_progress").html("亲，正在编译，请耐心等候...");
        },
         error: function (jqXHR, textStatus, errorThrown) {
            $("#build_progress").html("系统问题,请联系开发同事");
        },
        success: function(json){
            console.log(json);
            if (json['return'] == "success") {
                $("#build_progress").html(
                    "<span class='label label-success radius'>完成编译, 编译次数："
                    + json['build_number'] + "</span>");
            }
            if (json['return'] == "error") {
                $("#build_progress").html(
                "<span class='label label-error radius'>编译出错, 编译次数："
                + json['build_number'] + "</span>");
            }

        }
    });

});