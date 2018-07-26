CREATE TABLE `comments` (
	`comment_ID`	bigint(20)	NOT NULL,
	`comment_post_ID`	bigint(20)	NOT NULL	DEFAULT '0',
	`comment_author`	tinytext	NOT NULL,
	`comment_author_email`	varchar(100)	NOT NULL	DEFAULT '',
	`comment_date`	datetime	NOT NULL	DEFAULT '0000-00-00 00:00:00'	COMMENT '0000-00-00 00:00:00',
	`comment_date_gmt`	datetime	NOT NULL	DEFAULT '0000-00-00 00:00:00'	COMMENT '0000-00-00 00:00:00',
	`comment_content`	text	NOT NULL,
	`comment_type`	varchar(20)	NOT NULL	DEFAULT '',
	`user_id`	bigint(20)	NOT NULL	DEFAULT '0'
);

CREATE TABLE `users` (
	`ID`	bigint(20)	NOT NULL,
	`user_login`	varchar(60)	NOT NULL	DEFAULT '',
	`user_pass`	varchar(255)	NOT NULL	DEFAULT '',
	`user_nickname`	varchar(50)	NOT NULL	DEFAULT '',
	`user_email`	varchar(100)	NOT NULL	DEFAULT '',
	`user_registered`	datetime	NOT NULL	DEFAULT '0000-00-00 00:00:00',
	`user_status`	int(11)	NOT NULL	DEFAULT '0',
	`display_name`	varchar(250)	NOT NULL	DEFAULT ''
);

CREATE TABLE `posts` (
	`ID`	bigint(20)	NOT NULL,
	`post_author`	varchar(20)	NOT NULL	DEFAULT '0',
	`post_date`	datetime	NOT NULL	DEFAULT '0000-00-00 00:00:00',
	`post_content`	longtext	NOT NULL,
	`post_title`	text	NOT NULL,
	`post_status`	varchar(20)	NOT NULL	DEFAULT 'publish',
	`comment_status`	varchar(20)	NOT NULL	DEFAULT 'open'	COMMENT 'open',
	`post_password`	varchar(255)	NOT NULL	DEFAULT '',
	`post_name`	varchar(200)	NOT NULL	DEFAULT '',
	`post_modified`	datetime	NOT NULL	DEFAULT '0000-00-00 00:00:00',
	`post_type`	varchar(20)	NOT NULL	DEFAULT 'post',
	`comment_count`	bigint(20)	NOT NULL	DEFAULT '0'	COMMENT '0',
	`category_ID2`	bigint(20)	NOT NULL
);

CREATE TABLE `categories` (
	`category_ID`	bigint(20)	NOT NULL,
	`category_name`	varchar(100)	NOT NULL,
	`category_level`	int(1)	NOT NULL,
	`category_line`	int(5)	NOT NULL
);

ALTER TABLE `comments` ADD CONSTRAINT `PK_COMMENTS` PRIMARY KEY (
	`comment_ID`
);

ALTER TABLE `users` ADD CONSTRAINT `PK_USERS` PRIMARY KEY (
	`ID`
);

ALTER TABLE `posts` ADD CONSTRAINT `PK_POSTS` PRIMARY KEY (
	`ID`
);

ALTER TABLE `categories` ADD CONSTRAINT `PK_CATEGORIES` PRIMARY KEY (
	`category_ID`
);
