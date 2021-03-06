$(document).ready(function(){
 
    
    $("#srec-slider").slick({
      infinite: true,
      slidesToShow: 3,
      slidesToScroll: 1,
      dots: true,
      arrows: true,
      autoplay: true,
      autoplaySpeed: 3000,
      //infinite: true;
    });

    $("#fame-slider").slick({
      infinite: true,
      slidesToShow: 3,
      slidesToScroll: 1,
      dots: true,
      arrows: true,
      autoplay: true,
      autoplaySpeed: 3000,
      //infinite: true;
    });
    
    $(".slider").slick({
      infinite: true,
      slidesToShow: 3,
      slidesToScroll: 1,
      dots: true,
      arrows: true,
      autoplay: true,
      autoplaySpeed: 3000,
      //infinite: true;
    });


    $('#profile-create-form').addressfield({
      json: '/static/data/addressfield.json',
      fields: {
        country: '#id_country',
        locality: '#locality-fields',
        localityname: '#id_city',
        administrativearea: '#id_state',
        postalcode: '#id_zip_code'
      },
    });

    $('#profile-view-form').addressfield({
      json: '/static/data/addressfield.json',
      fields: {
        country: '#country',
        locality: '#locality-fields',
        localityname: '#city',
        administrativearea: '#state',
        postalcode: '#zip'
      },
    });



   
     $('#add_more').click(function() {
        cloneMore('#form-row', 'service');
    });
     function cloneMore(selector, type) {
        var newElement = $(selector).clone(true);
        
        var total = $('#id_' + type + '-TOTAL_FORMS').val();
        newElement.find(':input').each(function() {
            var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        });
        newElement.find('label').each(function() {
            var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
            $(this).attr('for', newFor);
        });
        total++;
        $('#id_' + type + '-TOTAL_FORMS').val(total);
        $(selector).after(newElement);
    }



    $("form#profile-create-form #id_professional-industry").change(function(){
       //console.log('changed')

       var selected = $( "#id_professional-industry option:selected" ).text();

       if(selected == 'Other'){
          $("form#profile-create-form #other-fieldset").show();
       }
    });



    $("form#profile-form #id_professional-industry").change(function(){
       //console.log('changed')

       var selected = $( "#id_professional-industry option:selected" ).text();

       if(selected == 'Other'){
          $("form#profile-form #other-fieldset").show();
       }
    });



    /** Member profile edit */
    $( "#edit-profile" ).click(function(e) {

      e.preventDefault();

      $(this).hide();

    });
});
