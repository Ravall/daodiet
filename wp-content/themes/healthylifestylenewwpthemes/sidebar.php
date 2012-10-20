<div class="span-6 last">
	<div id="topsearch" >
			<?php get_search_form(); ?>
	</div>

	<div class="sidebar">
		<ul>
			<?php
					if ( !function_exists('dynamic_sidebar') || !dynamic_sidebar() ) : ?>


				<li><h2><?php _e('Recent Posts'); ?></h2>
			               <ul>
					<?php wp_get_archives('type=postbypost&limit=5'); ?>
			               </ul>
				</li>

				<li><h2>Архивы</h2>
					<ul>
					<?php wp_get_archives('type=monthly'); ?>
					</ul>
				</li>

				<li>
					<h2>Календарь</h2>
					<?php get_calendar(); ?>
				</li>

				<?php wp_list_categories('hide_empty=0&show_count=1&title_li=<h2>Categories</h2>'); ?>

				<li id="tag_cloud"><h2>Метки</h2>
					<?php wp_tag_cloud('largest=16&format=flat&number=20'); ?>
				</li>

				<?php wp_list_bookmarks(); ?>

				<?php include (TEMPLATEPATH . '/recent-comments.php'); ?>
				<?php if (function_exists('get_recent_comments')) { get_recent_comments(); } ?>


				<li><h2>Мета</h2>
					<ul>
						<?php wp_register(); ?>
						<li><?php wp_loginout(); ?></li>
						<li><a href="http://gmpg.org/xfn/"><abbr title="XHTML Friends Network">XFN</abbr></a></li>
						<li><a href="http://wordpress.org/" title="Powered by WordPress, state-of-the-art semantic personal publishing platform.">WordPress</a></li>
						<?php wp_meta(); ?>
					</ul>
					</li>

			<?php endif; ?>
		</ul>
	</div>
</div>