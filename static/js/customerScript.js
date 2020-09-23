//labels and progress bar
$("#stepLinks div").click(function() {
  $(this).addClass('active').siblings().removeClass('active');
  var target = $(this).attr('href');
  $(target).removeAttr('hidden').siblings().attr('hidden','hidden');
  //$(this).css("border-bottom","5px solid #628bfc");
  if($(this).attr('id')=="personalLink"){
      $("#progress3").css("width","0%");
      $("#progress2").css("width","0%");
  }
  else if($(this).attr('id')=="educationalLink"){
      $("#progress2").css("width","100%");
      $("#progress3").css("width","0%");
  }
  else{
      $("#progress2").css("width","100%");
      //setTimeout(function(){},350);
      $("#progress3").css("width","100%");
  }
});

//customer registration form navigation
$("#personalNext").click(function(){
    var fields = $("[required]");
    var isValid = [];
    isValid.fill(0,0);
    var letters = /^[A-Za-z ]+$/;
    var genderValid = false;

    //gender check
    if ($("#maleRadio").is(':checked')==false && $("#femaleRadio").is(':checked')==false){
        $("#maleRadio").parent().parent().parent().addClass("redBorder");
        $(".genderWarn").html('<i class="material-icons align-middle pr-1">error_outline</i>'+"This is a required field.");  
        genderValid = false;
    }
    else{
        $("#maleRadio").parent().parent().parent().removeClass("redBorder");
        $(".genderWarn").html("");
        genderValid  = true;
    }
    
    //required check
    for(var i=0; i<fields.length; i++){
        if($(fields[i]).val()=="" || $(fields[i]).val()==null){
            $(fields[i]).css("border-color","#dc3545");
            $(fields[i]).siblings().html('<i class="material-icons align-middle pr-1">error_outline</i>'+"This is a required field.");
            isValid[i]=0;
        }
        else{
            //general if not empty
            $(fields[i]).css("border-color","#fcd462");
            $(fields[i]).siblings().html("");
            isValid[i]=1;

            //text fields
            if($(fields[i]).attr("type")=="text" && $(fields[i]).attr("name")!="barangay"){
                if($(fields[i]).val().match(letters)==null){
                    $(fields[i]).css("border-color","#dc3545");
                    $(fields[i]).siblings().html('<i class="material-icons align-middle pr-1">error_outline</i>'+"Must contain letters only.");
                    isValid[i]=0;
                }
                else{
                    $(fields[i]).css("border-color","#fcd462");
                    $(fields[i]).siblings().html("");
                    isValid[i]=1;
                }
            }

            //zipCode
            if($(fields[i]).attr("name")=="zipCode"){
                if($(fields[i]).val().length!=4){
                    $(fields[i]).css("border-color","#dc3545");
                    $(fields[i]).siblings().html('<i class="material-icons align-middle pr-1">error_outline</i>'+"Must be 4 digits.");
                    isValid[i]=0;
                }

                else{
                    $(fields[i]).css("border-color","#fcd462");
                    $(fields[i]).siblings().html("");
                    isValid[i]=1;
                }
            }
        }
    }
    if(isValid.includes(0) || genderValid==false);
    else{
        $("#educationalLink").addClass('active').siblings().removeClass('active');
        var target = "#educationalBackground";
        $(target).removeAttr('hidden').siblings().attr('hidden','hidden');
        $("#progress2").css("width","100%");
        $("html, body").animate({ scrollTop: 0 }, 500);
    }
});

$("#educationalPrevious").click(function(){
    $("#personalLink").addClass('active').siblings().removeClass('active');
    var target = "#personalInfo";
    $(target).removeAttr('hidden').siblings().attr('hidden','hidden');
    $("#progress2").css("width","0%");
    $("html, body").animate({ scrollTop: 0 }, 500);
});

$("#educationalNext").click(function(){
    $("#professionalLink").addClass('active').siblings().removeClass('active');
    var target = "#professionalBackground";
    $(target).removeAttr('hidden').siblings().attr('hidden','hidden');
    $("#progress3").css("width","100%");
    $("html, body").animate({ scrollTop: 0 }, 500);
});

$("#professionalPrevious").click(function(){
    $("#educationalLink").addClass('active').siblings().removeClass('active');
    var target = "#educationalBackground";
    $(target).removeAttr('hidden').siblings().attr('hidden','hidden');
    $("#progress3").css("width","0%");
    $("html, body").animate({ scrollTop: 0 }, 500);
});

//append entry to awards
$(".awardsCounter").change(function(){
    var count = $(this).val();
    var list = $(this).parent().siblings().children();
    var listCount = list.children().length
    if(count > listCount){
        var listitem = '<li><input type="text"class="form-control" placeholder="Award Description" required></li>';
        while(listCount!=count){
            list.append(listitem);
            listCount++;
        }
    }
    else{
        while(listCount!=count){
            list.children().last().remove();
            listCount--;
        }
    }
});

//append entry to trainings
$(".trainingsCounter").change(function(){
    var count = $(this).val();
    var list = $("#trainingsList");
    var listCount = list.children().length
    if(count > listCount){
        var listitem = 
        '<li>'+
        '<div class="form-row h6 pl-3 pt-2">Training</div>'+
        '<div class="form-row h6 pl-2">'+
            '<div class="col-6"><input type="text"class="form-control" placeholder="Title" required></div>'+
            '<div class="col-6"><input type="text"class="form-control" placeholder="Sponsor" required></div>'+
        '</div>'+
        '<div class="form-row h6 pl-2">'+
            '<div class="col-6"><input type="text"class="form-control" placeholder="Venue" required></div>'+
            '<div class="col-6"><input type="date"class="form-control" required></div>'+
        '</div>'+
        '</li>';
        while(listCount!=count){
            list.append(listitem);
            listCount++;
        }
    }
    else{
        while(listCount!=count){
            list.children().last().remove();
            listCount--;
        }
    }
});

//load image file chosen
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#profDisplay')
                .attr('src', e.target.result)
        };
        reader.readAsDataURL(input.files[0]);
    }
}

//loadTable
$(document).ready(function(){
    var table = $('#customerDataTable').DataTable({
        "dom": "<'row'<'col-sm-12 col-md-3'l><'col-sm-12 col-md-3 d-flex datefrombar'><'col-sm-12 col-md-3 d-flex datetobar'><'col-sm-12 col-md-3'f>>" +
        "<'row'<'col-sm-12'tr>>" +
        "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-2'B><'col-sm-12 col-md-2 addCustomerBar'><'col-sm-12 col-md-3'p>>",
        "oLanguage": {
            "sSearch": "Search:"
          },
        buttons: [
            {
               extend: 'excel',
               text: 'Excel',
               className: 'btn btn-success btn-block excelButton',
               exportOptions: {
                  columns: 'th:not(:last-child)'
               }
            }
         ],
        "columnDefs": [
            { "orderable": false, "targets": 5 }
        ]
    });
    $(".excelButton").parent().addClass("container p-0");
    //table.buttons().container().appendTo( '#menuBar' );
    var datefrom = '<span class="date-label mr-1 mt-1">From:</span><input type="date" class="form-control form-control-sm" id="datefrom"><i class="material-icons mt-1" id="clearfrom">close</i>';
    var dateto = '<span class="date-label mr-1 mt-1">To:</span><input type="date" class="form-control form-control-sm" id="dateto"><i class="material-icons mt-1" id="clearto">close</i>';
    //var addCustomerButton = '<input type="submit" value="Add Customer" class="btn btn-block btn-primary" id="addCustomer">';
    var addCustomerButton = '<a class="btn btn-block btn-primary" href="../customer/registration">Add Customer</a>';
    $(".datefrombar").append(datefrom);
    $(".datetobar").append(dateto);
    $(".addCustomerBar").append(addCustomerButton);
    $("#clearfrom").css("cursor","default").click(function(){ $("#datefrom").val(""); table.draw(); });
    $("#clearto").css("cursor","default").click(function(){ $("#dateto").val(""); table.draw(); });
    $.fn.dataTable.ext.search.push(
        function (settings, data, dataIndex) {
            var min = $('#datefrom').val();
            var max = $('#dateto').val();
            var startDate = data[0];
            if (min == "" && max == "") return true;
            if (min == "" && startDate <= max) return true;
            if (max == "" && startDate >= min) return true;
            if (startDate <= max && startDate >= min) return true;
            return false;
        }
    );
     $('#datefrom').select(function(){ table.draw(); });
     $('#dateto').select(function(){ table.draw(); });
    $('#datefrom, #dateto').change(function () {
        table.draw();
    });
});

//show delete modal
$(".deleteColor").click(function(){
    $("#deleteModal").modal('show');
});

/*show view modal
$(".viewColor").click(function(){
    $("#viewModal").modal('show');
    var viewInfo = $(this).parent().siblings();
    $("[name=dateRegField]").val($(viewInfo[0]).html());
    $("[name=firstField]").val($(viewInfo[1]).html());
    $("[name=lastField]").val($(viewInfo[2]).html());
    $("[name=birthField]").val($(viewInfo[3]).html());
    $("[name=cityField]").val($(viewInfo[4]).html());
});*/