
# Загружаем библиотеки
library(ggplot2)

freq <- read.csv(
		"output/tables/frequencies.csv",
		fileEncoding = "UTF-8"
)

# Берем ТОП-20 слов
top_words <- head(freq, 20)

# Строим график
plot <- ggplot(
				top_words,
				aes(
						x = reorder(word, count),
						y = count
				)
		) +
		geom_col() +
		coord_flip() +
		labs(
				title = "Топ-20 слов",
				x = "Слово",
				y = "Частота"
		)

# Сохраняем изображение
ggsave(
		"output/plots/top_words.png",
		plot,
		width = 8,
		height = 6
)

# Количество публикаций по СМИ

news <- read.csv(
		"data/news.csv",
		fileEncoding = "UTF-8"
)

media_counts <- as.data.frame(
		table(news$source)
)

colnames(media_counts) <- c(
		"source",
		"count"
)

plot2 <- ggplot(
				media_counts,
				aes(
						x = reorder(source, count),
						y = count
				)
		) +
		geom_col() +
		coord_flip() +
		labs(
				title = "Количество публикаций по СМИ",
				x = "Источник",
				y = "Количество публикаций"
		)

ggsave(
		"output/plots/media_sources.png",
		plot2,
		width = 8,
		height = 6
)

# Динамика публикаций по дням

news$date_only <- substr(news$date, 1, 11)

daily_counts <- as.data.frame(
		table(news$date_only)
)

names(daily_counts) <- c(
		"date",
		"count"
)

plot3 <- ggplot(
				daily_counts,
				aes(
						x = date,
						y = count,
						group = 1
				)
		) +
		geom_line(linewidth = 1) +
		geom_point(size = 3) +
		labs(
				title = "Динамика публикаций по дням",
				x = "Дата",
				y = "Количество публикаций"
		)

ggsave(
		"output/plots/daily_dynamics.png",
		plot3,
		width = 8,
		height = 6
)