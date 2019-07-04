# 4Dpredict-power-calculations
Power calculation for training and comparing models for cardiac motion analysis

The internal validation sample size is estimated based on a test of the null hypothesis *H<sub>0</sub>* : ΔC = 0 (with a two-sided alternative), where ΔC is the difference in Harrell’s concordance index between the deep learning and conventional parameter models. To compute the sample size, we will use an approach similar to the type applied in Obuchowski & McClish (1997) and Kang et al (2015), where a Wald-type test statistic is constructed for *H<sub>0</sub>*. For our case we will, for the sake of simplicity, assume that the magnitude of the standard error SE<sub>ΔC</sub> is roughly the same under the null and alternative hypotheses. Further, we will assume a (conservative) effect size of ΔC=0.06 (approximately half of that observed in our pilot study), and a standard error estimate of SE<sub>ΔC</sub> = 0.162, derived from model comparison simulations using a censoring rate of ~83%. With these assumptions, a minimum sample size of n=464 would be required to guarantee 90% power and n=800 for 99% power (at the 5% significance level). 

1.	Obuchowski N, McClish DK (1997) Sample size determination for diagnostic accuracy studies involving binomial ROC curve indices. Statistics in Medicine 16(13):1529
2.	Kang L, Chen W, Petrick NA, Gallas BD (2015) Comparing two correlated C indices with right-censored survival outcome: a one-shot nonparametric approach. Statistics in Medicine 34(4):685

