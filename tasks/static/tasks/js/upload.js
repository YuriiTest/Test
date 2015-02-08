$(document).ready(function()
{
    var uploadPreview = $("#uploadPreview");
    if (uploadPreview){
        var defaultImage =  uploadPreview.attr("src");
    }
    //123
    $("#id_select").change(function() {
        var selectedValue = $("#id_select").val();
        if (selectedValue === "")
        {
            uploadPreview.attr("src", defaultImage);
        }
        else
        {
            uploadPreview.attr("src", "/media/" + selectedValue);
        }
    });
    //456
    uploadImage.change(function() {
        var oFReader = new FileReader();
        oFReader.readAsDataURL(document.getElementById("uploadImage").files[0]);
        oFReader.onload = function (oFREvent) {
            if (oFREvent.target.result.indexOf("data:image") +1)
            {
                uploadPreview.attr("src", oFREvent.target.result);
            }
            else
            {
                uploadPreview.attr("src", "/static/tasks/img/no-image.png");
            }
        };
        $("#display").show();
    });
});