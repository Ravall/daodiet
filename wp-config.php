<?php
/**
 * Основные параметры WordPress.
 *
 * Этот файл содержит следующие параметры: настройки MySQL, префикс таблиц,
 * секретные ключи, язык WordPress и ABSPATH. Дополнительную информацию можно найти
 * на странице {@link http://codex.wordpress.org/Editing_wp-config.php Editing
 * wp-config.php} Кодекса. Настройки MySQL можно узнать у хостинг-провайдера.
 *
 * Этот файл используется сценарием создания wp-config.php в процессе установки.
 * Необязательно использовать веб-интерфейс, можно скопировать этот файл
 * с именем "wp-config.php" и заполнить значения.
 *
 * @package WordPress
 */

// ** Параметры MySQL: Эту информацию можно получить у вашего хостинг-провайдера ** //
/** Имя базы данных для WordPress */
define('DB_NAME', 'daodiet');

/** Имя пользователя MySQL */
define('DB_USER', 'daodiet_user');

/** Пароль к базе данных MySQL */
define('DB_PASSWORD', 'eYz1C8ro');

/** Имя сервера MySQL */
define('DB_HOST', 'localhost');

/** Кодировка базы данных для создания таблиц. */
define('DB_CHARSET', 'utf8');

/** Схема сопоставления. Не меняйте, если не уверены. */
define('DB_COLLATE', '');

/**#@+
 * Уникальные ключи и соли для аутентификации.
 *
 * Смените значение каждой константы на уникальную фразу.
 * Можно сгенерировать их с помощью {@link https://api.wordpress.org/secret-key/1.1/salt/ сервиса ключей на WordPress.org}
 * Можно изменить их, чтобы сделать существующие файлы cookies недействительными. Пользователям потребуется снова авторизоваться.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         '?T={Y8J1gn$sWi3n!L|&ub@byazc.T1o$<dR.Prx|.Z}qS<Fw=9pt~V>z]|XI3w4');
define('SECURE_AUTH_KEY',  'g+nK%kRL7FJ$^Z?+me }e-oIOKh?0@wlKj;kv^RIvU^P&JP@0?:G0+vYEg;Rv]~M');
define('LOGGED_IN_KEY',    ']cOzpTU}0=1bFk}sJ_jF`py(1n7Xp7.lBCb+-*s=-kot;kRkdEKaq fAtC+RuCyj');
define('NONCE_KEY',        '|8N9vQh2;0;B+vyGflLA_4rmEChA/|.&$4uxD@1X:hTDwtb72SB71kF9IX;]i]M7');
define('AUTH_SALT',        'a|:x-gpYm+If#I NdbAuGyax1*%o ^+H5+{&K5t;2Jwf0#-vG[CZ{tgyzy)G~Qmj');
define('SECURE_AUTH_SALT', 'Nt>5dCldL><hIMZ3%BRhSn%DkrIC_SEFa%j@tr|XB|HJ^[mFVKy%<O`cT[v<$H3K');
define('LOGGED_IN_SALT',   'zR~0js>VGEo,^{Slyo,G+H?Ebm`0->c~gucaOD;nYs8S@7[GI_-y):-Jza]15H;T');
define('NONCE_SALT',       'JHU[{?+Yb[_ui-q:vT9Ki&c*UD_c]]>i4!OLkQH-~r9MZSh1#G;!$D>|*)U|X+lz');

/**#@-*/

/**
 * Префикс таблиц в базе данных WordPress.
 *
 * Можно установить несколько блогов в одну базу данных, если вы будете использовать
 * разные префиксы. Пожалуйста, указывайте только цифры, буквы и знак подчеркивания.
 */
$table_prefix  = 'wp_';

/**
 * Язык локализации WordPress, по умолчанию английский.
 *
 * Измените этот параметр, чтобы настроить локализацию. Соответствующий MO-файл
 * для выбранного языка должен быть установлен в wp-content/languages. Например,
 * чтобы включить поддержку русского языка, скопируйте ru_RU.mo в wp-content/languages
 * и присвойте WPLANG значение 'ru_RU'.
 */
define('WPLANG', 'ru_RU');

/**
 * Для разработчиков: Режим отладки WordPress.
 *
 * Измените это значение на true, чтобы включить отображение уведомлений при разработке.
 * Настоятельно рекомендуется, чтобы разработчики плагинов и тем использовали WP_DEBUG
 * в своём рабочем окружении.
 */
define('WP_DEBUG', false);

/* Это всё, дальше не редактируем. Успехов! */

/** Абсолютный путь к директории WordPress. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Инициализирует переменные WordPress и подключает файлы. */
require_once(ABSPATH . 'wp-settings.php');
