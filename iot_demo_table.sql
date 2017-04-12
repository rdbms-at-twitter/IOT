CREATE TABLE `sensor` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `dev_id` varchar(32) NOT NULL,
  `temperature` varchar(10) NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
