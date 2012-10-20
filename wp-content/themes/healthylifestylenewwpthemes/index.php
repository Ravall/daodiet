<?php get_header(); ?>
		<div class="span-24" id="contentwrap">
			<div class="span-18">
				<div id="content">
					<?php if (have_posts()) : ?>
						<?php while (have_posts()) : the_post(); ?>

						<div <?php post_class() ?> id="post-<?php the_ID(); ?>">
							<h2 class="title"><a href="<?php the_permalink() ?>" rel="bookmark" title="Постоянная ссылка на <?php the_title_attribute(); ?>"><?php the_title(); ?></a></h2>
							<div class="postdate"><img src="<?php bloginfo('template_url'); ?>/images/date.png" /> <?php the_time('F jS, Y') ?> <img src="<?php bloginfo('template_url'); ?>/images/user.png" /> <?php the_author() ?> <?php if (current_user_can('edit_post', $post->ID)) { ?> <img src="<?php bloginfo('template_url'); ?>/images/edit.png" /> <?php edit_post_link('Редактировать', '', ''); } ?></div>

							<div class="entry">
<?php if ( function_exists("has_post_thumbnail") && has_post_thumbnail() ) { the_post_thumbnail(array(200,160), array("class" => "alignleft post_thumbnail")); } ?>
								<?php the_content('Читать далее &raquo;'); ?>
							</div>
							<div class="postmeta"><img src="<?php bloginfo('template_url'); ?>/images/folder.png" /> Добавлено в <?php the_category(', ') ?> <?php if(get_the_tags()) { ?> <img src="<?php bloginfo('template_url'); ?>/images/tag.png" /> <?php  the_tags('Метки: ', ', '); } ?>  <img src="<?php bloginfo('template_url'); ?>/images/comments.png" /> <?php comments_popup_link('Нет Комментариев &#187;', '1 Комментарий &#187;', '% Комментария(-ев) &#187;'); ?></div>
						</div><!--/post-<?php the_ID(); ?>-->

				<?php endwhile; ?>
				<div class="navigation">
					<div class="alignleft"><?php next_posts_link('&laquo; Предыдущие записи') ?></div>
					<div class="alignright"><?php previous_posts_link('Следующие записи &raquo;') ?></div>
				</div>
				<?php else : ?>
					<h2 class="center">Не Найдено</h2>
					<p class="center">Извините, но здесь нет того, что вы ищите.</p>
					<?php get_search_form(); ?>

				<?php endif; ?>
				</div>
			</div>

		<?php get_sidebar(); ?>
	</div>
<?php get_footer(); ?>
