library(ggplot2)


calibration_df <- read.csv('calibration.csv', row.names=1)
calibration_df$test <- factor(calibration_df$test, levels=c('q3', 'arht', 'pillai'))
p_cal <- ggplot(calibration_df) +
	aes(x=pp, y=pval, color=test) + 
	geom_line(alpha=0.8) + 
	geom_abline(alpha=0.4, linetype=2) + 
	labs(x = "Type I Error", y = "Significance Level") +
	scale_color_discrete(labels=c(arht="ARHT", pillai="Pillai-Bartlett Trace", q3=latex2exp::TeX("Hotelling's $T^2$"))) + 
	theme_minimal(base_size=8) +
	theme(legend.position = 'none', legend.title=element_blank(), legend.text=element_text(size=8))

leg <- cowplot::get_legend(p_cal + theme(legend.position='bottom'))
p_cal <- cowplot::add_sub(p_cal, "(a)", size=8)

# ggsave('calibration.pdf', plot=p_cal, width=2.5, height=2, units='in')

accuracy_df <- read.csv('accuracy.csv', row.names=1)
accuracy_df$test <- factor(accuracy_df$test, levels=c('rf_q3', 'rf_arht', 'rf_pillai'))
p_acc <- ggplot(accuracy_df) +
	 aes(x=effect_xy, y=acc, ymin = acc - error,
	     ymax = acc + error, color=test, fill = test) +
	 geom_line() +
	 geom_point(pch=19, size=1, show.legend=F) +
	 geom_ribbon(alpha=0.4, linetype=0, show.legend=F) + 
	 ylim(0.45, 0.7) +
	 labs(y = "Accuracy (%)", x = "Effect (Log Scale)") + 
	 scale_color_discrete(labels=c(rf_arht="ARHT", rf_pillai="Pillai's Trace", rf_q3=latex2exp::TeX("Hotelling's $T^2$"))) + 
	 theme_minimal(base_size = 8) + 
	 theme(legend.position = 'none', legend.title=element_blank())

p_acc <- cowplot::add_sub(p_acc, "(b)", size=8)
# ggsave('accuracy.pdf', plot=p_acc, width=2.5, height=2, units='in')

p <- cowplot::plot_grid(p_cal, p_acc, ncol=2, align='hv')
g <- cowplot::plot_grid(leg, p, ncol = 1, rel_heights = c(0.1, 0.8))
ggsave('conclusion.pdf', plot=g, width=5, height=1.5)
